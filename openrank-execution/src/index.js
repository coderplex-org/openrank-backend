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
    command: "",
    interpreted: false,
    compile: "gcc"
  },
  java: {
    extension: "java",
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
  const { lang, code } = req.body;
  fs.writeFile(`temp.${langMeta[lang].extension}`, code, err => {
    if (err) console.log(err);
    else console.log("Successfully Written to File.");
  });
  if (langMeta[lang].interpreted) {
    exec(
      `${langMeta[lang].command} temp.${langMeta[lang].extension}`,
      { timeout: 1000 },
      (err, stdout, stderr) => res.send({ err, stderr, stdout })
    );
  } else {
    exec(
      `${langMeta[lang].compile} temp.${langMeta[lang].extension}`,
      (err, stdout, stderr) => {
        if (stderr == null && err == null) {
          exec(
            `${langMeta[lang].command} ./temp.${langMeta[lang].extension}`,
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

app.listen(8001, () => {
  console.log("Example app listening on port 8001!");
});
