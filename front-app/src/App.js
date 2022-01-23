import './App.css';

const MusicVideo = () => {
	return (
		<div className={'the_video'}>
			<iframe width="800" height="800" src="http://0.0.0.0:8000/youtube/view" />
		</div>
	);
};

function App() {
	return <MusicVideo />;
}

export default App;
