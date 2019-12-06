$.getJSON("/data").done(makeList);
var jsonData;

function makeList(jsonData) {
    for (element of jsonData) {
        let item = `<li><div class="accessmodifier">${element.access_modifier}</div> <div class="keyword">${element.keyword}</div> <div class="datatype">${element.data_type}</div> <div class="identifier">${element.identifier}</div></li>`
        $("#list").append(item);
    }
}

function sortList() {
    makeSortedList(jsonData);
}

function makeSortedList(jsonDataIn){
    jsonData = jsonDataIn
    $("#list").empty()
    let word = $("#text").val()
    for (element of jsonData) {
        let elmentData = `${element.access_modifier} ${element.keyword} ${element.data_type} ${element.identifier}`
        let item = `<li><div class="accessmodifier">${element.access_modifier}</div> <div class="keyword">${element.keyword}</div> <div class="datatype">${element.data_type}</div> <div class="identifier">${element.identifier}</div></li>`
        if (elmentData.includes(word) || word == "") {
            $("ul").append(item);
        }
    }
}
