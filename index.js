const express = require('express')

const app = express()

app.get('/',(req,res) => {
	res.send('Hi There I am testing 2 ')
})

app.listen(8080,()=>{
	console.log("Hi I am Listening on port 8080");
})