{
	"name": "hvgrid-Grid",
	"displayName": "Grid",
	"version": 1,
	"definition": "hvgrid/Grid/Grid.js",
	"libraries": [
	    {
            "name": "bootstrap.min.css",
            "version": "1",
            "mimetype": "text/css",
            "url": "hvgrid/Grid/bootstrap/css/bootstrap.min.css"
        }
	],
	"model":
	{
		"columns": { "type": "column[]", "droppable": true, "pushToServer": "shallow", "elementConfig": { "pushToServer": "shallow" } },
		"currentPage": { "type": "int", "default": 1, "tags": { "scope": "runtime" }, "pushToServer": "shallow" },
		"foundset": { "type": "foundset","default" : {"foundsetSelector":""} , "pushToServer": "allow", "initialPreferredViewPortSize": 130, "sendSelectionViewportInitially": true },
		"pageSize": { "type": "int", "default": 20 },
		"columnsPerRow": { "type": "int", "default": 3 },
		"template": { "type": "dataprovider" },
		"columnCssClass": { "type": "string", "default": "col" },
		"rowCssClass": { "type": "string", "default": "row" },
		"onCellClick": { "type": "function" }
	},
	"types": {
		"column": {
			"dataprovider": { "type": "dataprovider", "forFoundset": "foundset", "resolveValuelist" : true , "tags": { "useAsCaptionInDeveloper" : true, "captionPriority" : 2 }},
			"format": { "for": ["valuelist", "dataprovider"], "type": "format" },
			"headerStyleClass": { "type": "styleclass" },
			"headerText": { "type": "tagstring", "tags": { "useAsCaptionInDeveloper" : true, "captionPriority" : 1, "showInOutlineView": true }},
			"styleClass": { "type": "styleclass" },
			"styleClassDataprovider": { "type": "dataprovider", "forFoundset": "foundset" },
			"showAs": { "type": "string", "default": "text", "values": ["text", "html", "sanitizedHtml"] }
		}
    },
    "api": {
        "init": {
            "returns": "boolean",
            "parameters": [{ "name": "template", "type": "object"}]
        }
    }
}