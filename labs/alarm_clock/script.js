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

console.log("script is running...");

//#1
function My_Alarm(name){
    let time = "7:00am"
    console.log("Hey, " + name + " , wake up! It's " + time);
    
}

My_Alarm("Edgar");

//#2
function mom_Alarm(name2){
    let time = "6:00pm"
    console.log("Hey, " + name2 + " , wake up! It's " + time);
};

mom_Alarm("Mom");

function family_Alarm(name, time){
    console.log("Hey, " + name + " , wake up! It's " + time);
};

//#3
family_Alarm("Mom", "6:00pm");

function important_Alarm(message){
    console.log(message.toLocaleUpperCase());
};

important_Alarm("wake up, wake up, wake UP!!");


//#5
//How we did it
function snooze_Alarm(time){
    console.log("the alarm for " + time+":00am" + " has been changed to " + (time+1)+":00am");
};
snooze_Alarm(8);

//Actually how to do it
function alarm(num){
    var Newnum = num + 1
    console.log("the alarm for " + num + " has been changed to " + Newnum);
};

alarm(6);