function print(string){
  console.log(string)
}
const fs = require("fs");

answerList=[]
allowedList=[]
var inputs=["texts","midge","break","hello","lynch","adieu"]
var found=false
var word
var triesLeft=6
var input

async function getFile(file){
  return await fs.promises.readFile(file, "utf-8")
}

async function getWords(){

  data = await getFile("./wordle-allowed-guesses.txt")
  allowedList=data.split(/\r\n|\n\r|\n|\r/)
  data =  await getFile("./wordle-answers-alphabetical.txt")
  answerList=data.split(/\r\n|\n\r|\n|\r/)
  word= answerList[Math.floor(Math.random()*answerList.length)];
}

function inputCheck() {
  if (input.length==5){
    if (allowedList.includes(input)){
      allowed=true
    }
  }
}

function inputProcessing(){
  inputList=input.split("")
  print(inputList)
  wordList=word.split("")
  print(wordList)
  triesLeft=triesLeft-1
  for (let i = 0; i < 5; i++) {
    if (inputList[i]==wordList[i]){
      output[i]="Y"
    }
  }
  for (let i = 0; i < 5; i++) {
    if (wordList.includes(inputList[i])){
      if (foundLetters.includes(inputList[i])==false){
        if (output[i]!="Y"){
          output[i]="C"
        }
      }
    }
  }
}

async function main(){
  await getWords()
  
  while (triesLeft>0 && found==false){
    input=inputs[triesLeft-1]
    output=["N","N","N","N","N"]
    foundLetters=[]
    allowed=false
    inputCheck()
    if (allowed){
      print(triesLeft)
      inputProcessing()
    }else{
      print("INVALID IMPUT")
    }
    print(output)
  }
}

main()
