const SearchBar = require('./components/SearchBar');
const BrowserWindow = require('./components/BrowserWindow');

document.addEventListener('DOMContentLoaded', () => {
    const searchBar = new SearchBar();
    const browserWindow = new BrowserWindow();

    document.body.appendChild(searchBar.render());
    document.body.appendChild(browserWindow.render());

    searchBar.onSearch((query) => {
        browserWindow.loadResults(query);
    });
});