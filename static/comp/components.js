//Sidebar with Navigation at the left
class Sidebar extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() { // TODO: replace string with loadHTML('comp/sidebar.html');
        this.innerHTML = `
        <aside>
            <div class="logo-wrapper">
                <a href="#home">
                    <img src="/static/images/chair.png" alt="logo" class="logo-icon">
                    <h5 class="logo-text">Sitzplan Generator</h5>
                </a>
            </div>
            <nav><ul class="sidebar-menu">
                <li class="sidebar-header">NAVIGATION</li>
                <li><a href="#home">
                    <i class="material-icons text-icon">home</i> <span>Home</span>
                </a></li>
                <li><a href="#seating">
                    <i class="material-icons text-icon">chair_alt</i> <span>Create Seating</span>
                </a></li>
                <li><a href="#student">
                    <i class="material-icons text-icon">groups</i> <span>Student List</span>
                </a></li>
                <li><a href="#room">
                    <i class="material-icons text-icon">table_restaurant</i> <span>Classrooms</span>
                </a></li>
                <li><a href="#about">
                    <i class="material-icons text-icon">info</i> <span>About</span>
                </a></li>
            </ul></nav>
        </aside>
        `
    }
}

//Register components
customElements.define('left-sidebar', Sidebar);