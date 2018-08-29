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

var recipe = []; /* set recipe equal to an empty array*/;

function addInstructions(recipeArray){
// add all of the instructions into the recipeArray variable
recipeArray.push("1.Heat oven to 425ºF. Prepare Double-Crust Pastry.",
"2.Mix sugar, flour, cinnamon, nutmeg and salt in large bowl.",
"3.Stir in apples.",
"4.Turn into pastry-lined pie plate. Dot with butter. Trim overhanging edge of pastry 1/2 inch from rim of plate.",
"5.Roll other round of pastry. Fold into fourths and cut slits so steam can escape.",
"6.Unfold top pastry over filling; trim overhanging edge 1 inch from rim of plate.",
"7.Fold and roll top edge under lower edge, pressing on rim to seal; flute as desired.",
"8.Cover edge with 3-inch strip of aluminum foil to prevent excessive browning. Remove foil during last 15 minutes of baking.",
"9.Bake 40 to 50 minutes or until crust is brown and juice begins to bubble through slits in crust. Serve warm if desired.");




//return the array
}

function checkStep(num){
//return the correct step in the given array
return recipe[num];
}

//Write a function checkLength

function checkLength(recipeArray){
    console.log(recipeArray.length);
}


//Write a function publishRecipe

function publishRecipe(recipeArray){
    for(let i = 0; i < recipeArray.length;i++)
	console.log(recipeArray[i]);

}