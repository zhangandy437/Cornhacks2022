import './App.css';

const MusicVideo = () => {

    return (
        <div className={'the_video'}>
            <iframe width="800" height="800" src='http:127.0.0.1:8000/youtube/stichVideo/' />
        </div>
    );
}

function App() {
    return (
        <MusicVideo/>
    );
}

export default App;
