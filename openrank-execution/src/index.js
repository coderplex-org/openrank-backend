import express from "express";
import cors from "cors";
// import routes from './routes'

const fs = require("fs");
const { exec } = require("child_process");

console.log("Starting OpenRank Execution Server");

const app = express();
app.use(cors());
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

//Add handlers for routes here

//Lang specific meta, we have to configure this manually for now
const langMeta = {
  python3: {
    extension: "py",
    command: "py",
    interpreted: true
  },
  python2: {
    extension: "py",
    command: "python",
    interpreted: true
  },
  c: {
    extension: "c",
    defaultExecName: "a",
    execExtension: "exe",
    command: "",
    interpreted: false,
    compile: "gcc"
  },
  java: {
    extension: "java",
    defaultExecName: "",
    execExtension: "",
    command: "java",
    interpreted: false,
    compile: "javac"
  }
};

app.post("/", (req, res) => {
  //NOTE: Experimentation code
  /*
  This route takes the language and code from request and executes
  it by spawning a child process based on the meta-data 
  available for a given language
  */
  const { lang, code, filename } = req.body;
  fs.writeFile(`${filename}.${langMeta[lang].extension}`, code, err => {
    if (err) console.log(err);
    else console.log("Successfully Written to File.");
  });
  if (langMeta[lang].interpreted) {
    exec(
      `${langMeta[lang].command} ${filename}.${langMeta[lang].extension}`,
      { timeout: 1000 },
      (err, stdout, stderr) => res.send({ err, stderr, stdout })
    );
  } else {
    console.log("compiled lang");
    exec(
      `${langMeta[lang].compile} ${filename}.${langMeta[lang].extension}`,
      (err, stdout, stderr) => {
        if (!stderr && !err) {
          const { execExtension, defaultExecName } = langMeta[lang];
          const execFilename =
            (defaultExecName || filename) +
            (execExtension ? `.${execExtension}` : ``);
          console.log(
            `command for execution: ${langMeta[lang].command} ${execFilename}`
          );
          exec(
            `${langMeta[lang].command} ${execFilename}`,
            { timeout: 1000 },
            (err, stdout, stderr) => res.send({ err, stderr, stdout })
          );
        } else {
          res.send({ err, stderr, stdout });
        }
      }
    );
  }
  //TODO: Add logic to compare output with testcases saved in db before sending the response.
});

app.listen(9000, () => {
  console.log("Example app listening on port 9000!");
});
