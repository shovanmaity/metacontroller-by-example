const express = require("express");
const bodyParser = require('body-parser');

const PORT = 8080;
const app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json())

app.post("/sync", (req, res) => {
    let observed = req.body;
    let desired = {children: []};

    try {
        // observed ping object
        let ping = observed.parent;
        let name
        try{
            name = ping.spec.name
        }catch(e){
            name = "Unknown"
        }
        let pong =  {
            apiVersion: 'example.com/v1',
            kind: 'Pong',
            metadata: {
                name: ping.metadata.name
            },
            spec: {
                message: "Hello "+ name +" !!"
            }
        }
        // Generate desired children
        desired.children = [
            pong
        ];
        res.status(200).send(desired)
    } catch (e) {
        res.status(500).send({body: e.stack})
    }
});

app.listen(PORT, () => {
 console.log(`Server is listening on port: ${PORT}`);
});
