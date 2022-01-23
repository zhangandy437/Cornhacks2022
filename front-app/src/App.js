import './App.css';
import video from './videoFolder/SkiVideo.mp4';

const MusicVideo = () => {
    return (
        <div className={'the_video'}>
            <iframe width='75%' height='75%' src={video} />
        </div>
    );
}

function App() {
    return (
        <MusicVideo/>
    );
}

export default App;
