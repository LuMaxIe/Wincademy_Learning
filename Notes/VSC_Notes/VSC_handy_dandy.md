# Mix of useful Visual Studio Code facts

## Integrated terminal

Run code -r "filename.extension" to open a file in the same window

## Snippets 

Go to Code > Preferences > User snippets to add language specific snippets
i.e for .md files I added:
	"Python_code_example": {
		"prefix": "PY",
		"body": [
			"```Python\n$0\n```"
		],
		"description": "Adds a python code block"
	}
}