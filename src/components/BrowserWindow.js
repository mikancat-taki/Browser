import React from 'react';

const BrowserWindow = ({ searchResults }) => {
    return (
        <div className="browser-window">
            <h2>検索結果</h2>
            <ul>
                {searchResults.map((result, index) => (
                    <li key={index}>
                        <a href={result.link} target="_blank" rel="noopener noreferrer">
                            {result.title}
                        </a>
                        <p>{result.snippet}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default BrowserWindow;