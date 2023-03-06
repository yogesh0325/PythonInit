{
    "filter": {
        "$and":[
            { "hidden":false },
            { "type":"file" }
        ]
    },
    "join": {
        "filter": {
            "$and":[
                { "creator": { "$in":["yogesh.b@dataloop.ai"] } },
                { "label": { "$in":["Eye"] } }
            ]
        },
        "on": {
            "resource":"annotations",
            "local":"itemId",
            "forigen":"id"
        }
    }
}
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