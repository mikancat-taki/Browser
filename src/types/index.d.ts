interface SearchResult {
    title: string;
    link: string;
    snippet: string;
}

interface SearchQuery {
    query: string;
    results: SearchResult[];
}

interface BrowserWindowProps {
    results: SearchResult[];
}

interface SearchBarProps {
    onSearch: (query: string) => void;
}