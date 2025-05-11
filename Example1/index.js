let homeScore = document.getElementById("home-Score")
let guestScore = document.getElementById("guest-Score")
let varHomeScore = 0
let varGuestScore = 0
let titleHome = document.getElementById("title-home")
let titleGuest = document.getElementById("title-guest")
let previousGame = document.getElementById("previousGames")
function addHomeScore1(){
    varHomeScore += 1
    homeScore.textContent = varHomeScore
    whoIsWinning()
}

function addHomeScore2(){
    varHomeScore += 2
    homeScore.textContent = varHomeScore
    whoIsWinning()
}

function addHomeScore3(){
    varHomeScore += 3
    homeScore.textContent = varHomeScore
    whoIsWinning()
}

function addGuestScore1(){
    varGuestScore += 1
    guestScore.textContent = varGuestScore
    whoIsWinning()
}

function addGuestScore2(){
     varGuestScore += 2
     guestScore.textContent = varGuestScore
     whoIsWinning()
}

function addGuestScore3(){
     varGuestScore += 3
     guestScore.textContent = varGuestScore
     whoIsWinning()
}

function whoIsWinning(){
    resetTitle()
    if (varHomeScore > varGuestScore){
        titleHome.style.color = "green"
        titleHome.style.textShadow = "0px 0px 5px green"
        titleGuest.style.color = "#d62828"
        
    }else if(varHomeScore < varGuestScore){
        titleGuest.style.color = "green"
        titleGuest.style.textShadow = "0px 0px 4px green"
        titleHome.style.color = "#d62828"
    }else{
        resetTitle()
    }
}

function resetTitle(){
    titleHome.style.color = "white"
    titleHome.style.textShadow = "none"
    titleGuest.style.color = "white"
    titleGuest.style.textShadow = "none"
}

function newGame(){
    previousGame.textContent += "Home " +varHomeScore +" - " +varGuestScore + " Guest" +  " ||"
    varGuestScore = 0
    varHomeScore = 0
    resetTitle()
    homeScore.textContent = 0
    guestScore.textContent = 0
}