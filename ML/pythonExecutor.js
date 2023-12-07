const { exec } = require('child_process');

function executePythonScript(scriptPath, callback) {
  exec(`python ${scriptPath}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing Python script: ${error}`);
      callback(null);
      return;
    }

    // Assuming the Python script prints JSON to stdout
    try {
      const result = JSON.parse(stdout);
      callback(result);
    } catch (parseError) {
      console.error(`Error parsing Python script output: ${parseError}`);
      callback(null);
    }
  });
}

module.exports = {
  executePythonScript,
};
