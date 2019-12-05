$.getJSON("/data").done(makeList);

function makeList(jsonData) {
    for (element of jsonData) {
        let item = `<li><div class="access">${element.access}</div> <div class="type">${element.type}</div> <div class="identificator">${element.identificator}</div></li>`;
        $("ul").append(item);
    }
}