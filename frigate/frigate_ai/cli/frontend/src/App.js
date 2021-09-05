import Card from '@material-ui/core/Card';
import { makeStyles } from '@material-ui/core/styles';
import React, { useCallback, useState } from 'react';
import { useDropzone } from 'react-dropzone';
import './App.css';
import data from './data.json';
import Button from '@material-ui/core/Button';
import { colors } from '@material-ui/core'; 
import { uploadFile } from 'react-s3';

const config = {
  bucketName: data.S3_BUCKET,
  region: data.REGION,
  accessKeyId: data.ACCESS_KEY,
  secretAccessKey: data.SECRET_ACCESS_KEY,
}

const useStyles = makeStyles({
  card: {
    height: '90vh',
    width: '90vw',
    borderRadius: '20px',
    filter: 'drop-shadow(0px 0px 15px)',
    overflow: 'scroll'
  },
  title: {
    textAlign: 'left',
    marginLeft: '3%',
    marginRight: '3%',
    fontWeight: '500',
  },
  author: {
    textAlign: 'left',
    marginLeft: '3%',
    marginRight: '3%',
    fontWeight: '300',
  }, 
  description: {
    textAlign: 'left',
    marginLeft: '3%',
    marginRight: '3%',
    fontWeight: '300',
  },
  dropzone: {
    backgroundColor: '#eee',
    marginLeft: '3%',
    marginRight: '3%',
    marginBottom: '3%',
    borderRadius: '20px',
    height: '30vh',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center'
  },
  runButton: {
    backgroundColor: 'orange',
    width: '10vw',
    height: '5vh'
  }
});

function App() {
  const classes = useStyles(); 
  const [file, setFile] = useState(null);

  const onDrop = useCallback(acceptedFiles => {
    if (acceptedFiles.length > 0) {
      setFile(acceptedFiles[0]);
    }
  }, []);

  const upload = async () => {
    uploadFile(file, config)
        .then(data => console.log(data))
        .catch(err => console.error(err));
  }

  const {getRootProps, getInputProps, isDragActive} = useDropzone({onDrop});

  return (
    <div className="App">
      <header className="App-header">
        <Card className={classes.card}>
          <h1 className={classes.title}>
            {data.title}
          </h1>
          <h4 className={classes.author}>
           By <a href="https://en.wikipedia.org/wiki/Jimmy_O._Yang#:~:text=Yang%20(Chinese%3A%20%E6%AD%90%E9%99%BD%E8%90%AC%E6%88%90,HBO%20comedy%20series%20Silicon%20Valley.">
             {data.author}
            </a>
          </h4>
          <p className={classes.description}>
            {data.description}
          </p>
          <div className={classes.dropzone} {...getRootProps()}>
            <input {...getInputProps()} />
            {
              file == null ? 
                (isDragActive ?
                  <p>Release to Add Input File</p> :
                  <p>Drag In / Click to Add Input File</p>) : 
                file.name
            }
          </div>
          <Button className={classes.runButton} onClick={upload} disabled={file == null}>
            Run Model
          </Button>
        </Card>
        {/* <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
      </header>
    </div>
  );
}

export default App;
