const express = require('express')
const os = require('os');


const app = express()

const version = "V1.0.1"

app.get('/',(req,res) => {
	resp = 'Hi welcome to Sample node App : ' + version
	res.json({
	  "Hi welcome to Sample node App": version
	});

})

app.get('/add',(req,res) => {
	
	offset = 10000 
	num1 = Number.parseInt(req.query.num1 || 0)
	num2 = Number.parseInt(req.query.num2 || 0)
	result = num1 + num2 + offset
	res.json({
	  message: `addition of ${num1} + ${num2} with offset of ${offset}`,
	  result: result
	});

})

app.get('/mul',(req,res) => {
	
	num1 = Number.parseInt(req.query.num1 || 1)
	num2 = Number.parseInt(req.query.num2 || 1)
	result = num1 * num2

	res.json({
	  message: `Multiplication of ${num1} * ${num2}`,
	  result: result
	});

})

app.get('/whoami', (req, res) => {
  
  const ipAddresses = Object.fromEntries(Object.entries(os.networkInterfaces()).map(([key, val]) => [key, val.find(entry => entry.family === 'IPv4').address]));

  const userInfo = {
    user: os.userInfo().username,
    hostname: os.hostname(),
    platform: os.platform(),
    arch: os.arch(),
    Ips: ipAddresses
  };

  res.json(userInfo);
});
app.listen(8080,()=>{
	console.log("Hi I am Listening on port 8080");
})