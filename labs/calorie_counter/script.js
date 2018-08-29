// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Use querySelector to store the div in a variable.
let redButton = document.querySelector('#red', '#responseBox');

// Use addEventListener to respond to a click event.
redButton.addEventListener('click', e => {
    responseBox.style.backgroundColor = 'Red';
    responseBox.innerHTML='REEEEEEEEEEEEEEEEEEED';
  console.log("You clicked the red button!");
})

let greenButton = document.querySelector('#green', "#responeBox");

greenButton.addEventListener('click', e => {
    responseBox.style.backgroundColor='Green';
    responseBox.innerHTML='GREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEN';
    console.log("You clicked the green button!");
})

let blueButton = document.querySelector('#blue', '#responseBox');

blueButton.addEventListener('click', e =>{
    responseBox.style.backgroundColor='Blue';
    responseBox.innerHTML='BLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUEEEEEEEEEEEEEEEEEEEE';
    console.log("You clicked the blue button!")
})

let clearButton = document.querySelector('#grey','#responseBox');

clearButton.addEventListener('click', e =>{
    responseBox.style.backgroundColor='white';
    responseBox.innerHTML='';
})

