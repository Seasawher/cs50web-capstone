function App() {
    const [quizzes, setQuizzes] = React.useState([]);

    function dataFetch() {
        fetch('/api/quiz/', { method: 'GET' })
            .then(res => res.json())
            .then(data => {
                setQuizzes(data)
            })
    }

    // use "React.useEffect" to avoid re-rendering forever...!
    React.useEffect(() => {
        dataFetch();
    }, []);

    if (quizzes.length == 0) {
        return (
            <div className="max-w-2xl mx-auto">now loading..</div>
        );
    } else {
        return (
            <div>
                {quizzes.map(function (quiz) {
                    return <Quiz
                        key={quiz['id']}
                        author={quiz['user']['username']}
                        state="solved"
                        title={quiz['title']}
                        timestamp={formatTime(quiz['created_at'])}
                    />
                })}
            </div>
        );
    }
}

function Quiz({ author, state, title, timestamp }) {
    return (
        <div className="py-6 px-8 mb-3 bg-slate-700 rounded-lg max-w-2xl mx-auto">
            <div className="text-emerald-300 inline text-sm mr-2">
                <CheckCircleIcon className="inline w-4 h-4 mr-1" />
                {state}
            </div>
            <div className="inline text-sm">
                <StarIcon className="inline w-4 h-4 mr-1" />
                0
            </div>
            <div className="text-sky-300 font-bold text-xl mb-2">{title}</div>
            <div className="text-right text-xs">
                <span className=" text-slate-400 mr-2">{author}</span>
                <span className="">{timestamp}</span>
            </div>
        </div>
    );
}
const container = document.getElementById('root');
const root = ReactDOM.createRoot(container);
root.render(<App />);
