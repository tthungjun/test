const Avengers = ["Hulk", "IronMan", "Thor", "CaptianAmerica", "Blacwwidow"];
console.log(Avengers);
Avengers.push("Hawkeye");
console.log(Avengers);

const player = {
    name : "HSJ",
    age : 21,
    major : "CSE",
    something : null,
    football: function (player, back_num) {
        console.log(player + " " + back_num);
    }
};
console.log(player);
console.log(player.major);
player.age = 19;
player.univesity = "KHU";
player.something = "23th";
console.log(player);

// function
function landing(a) {
    console.log("I am " + a);
}
landing(Avengers[1]);

function football(player, back_num) {
    alert(player + " " + back_num);
}
football("Messi", 10);
football("Ronaldo", 7);
player.football(player.name, 39);

// return
function calculater (age1) {
    age1 + 2;
    return "hello";
}

const age2 = calculater(45);
console.log(age2);