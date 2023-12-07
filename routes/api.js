const express = require('express');
const router = express.Router();
const pythonExecutor = require('../ML/pythonExecutor');

router.get('/', (req, res) => {
  const scriptPath = 'ML/ForecastAPI.py';

  pythonExecutor.executePythonScript(scriptPath, (result) => {
    if (result) {
      res.json(result);
    } else {
      res.status(500).send('Error executing Python script');
    }
  });
});

// New endpoint to create generate forecast button
router.get('/run-forecast-script', (req, res) => {
  const scriptPath = 'ML/ForecastAPI.py';

  pythonExecutor.executePythonScript(scriptPath, (result) => {
    if (result) {
      res.json(result);
    } else {
      res.status(500).send('Error executing Python script');
    }
  });
});

module.exports = router;
