package main

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"net/http"

	"k8s.io/apimachinery/pkg/apis/meta/v1/unstructured"
)

type SyncRequest struct {
	Parent   unstructured.Unstructured `json:"parent"`
	Children Children                  `json:"children"`
}

type Children struct {
	Pongs []unstructured.Unstructured `json:"example.com/v1.Pong"`
}

type SyncResponse struct {
	Children []unstructured.Unstructured `json:"children"`
}

func sync(req *SyncRequest) (*SyncResponse, error) {
	res := &SyncResponse{}
	name, found, err := unstructured.NestedString(req.Parent.UnstructuredContent(),
		"spec", "name")
	if err != nil || !found {
		name = "Unknown"
	}

	chield := unstructured.Unstructured{
		Object: map[string]interface{}{
			"apiVersion": "example.com/v1",
			"kind":       "Pong",
			"metadata": map[string]interface{}{
				"name": req.Parent.GetName(),
			},
			"spec": map[string]interface{}{
				"message": "Hello " + name,
			},
		},
	}
	res.Children = append(res.Children, chield)
	return res, nil
}

func syncHandler(w http.ResponseWriter, r *http.Request) {
	body, err := ioutil.ReadAll(r.Body)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	req := &SyncRequest{}
	if err := json.Unmarshal(body, req); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	res, err := sync(req)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	body, err = json.Marshal(&res)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	w.Write(body)
}

func main() {
	http.HandleFunc("/sync", syncHandler)

	log.Fatal(http.ListenAndServe(":8080", nil))
}
