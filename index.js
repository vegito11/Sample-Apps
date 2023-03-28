const express = require('express')

const app = express()

app.get('/',(req,res) => {
	res.send('Hi There I am testing 4 ')
})

app.listen(8080,()=>{
	console.log("Hi I am Listening on port 8080");
})