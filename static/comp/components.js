//Header at the top
class Header extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        fetch('/header')
        .then((response) => response.text())
        .then((html) => {
            this.innerHTML =  html;
        })
        .catch((error) => {
            console.warn(error);
        });
    }
}

//Sidebar with Navigation at the left
class Sidebar extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        fetch('/sidebar')
        .then((response) => response.text())
        .then((html) => {
            this.innerHTML =  html;
        })
        .catch((error) => {
            console.warn(error);
        });
    }
}

//Register components
customElements.define('left-sidebar', Sidebar);
customElements.define('top-header', Header);