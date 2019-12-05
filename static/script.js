$.getJSON("/data").done(makeList);

function makeList(jsonData) {
    for (element of jsonData) {
        let keywords = ""
        for (keyword of element.types) {
            keywords += `<div class="keyword">${keyword}</div> `
        }
        let item = `<li>${keywords} <div class="identificator">${element.identificator}</div></li>`
        $("ul").append(item);
    }
}