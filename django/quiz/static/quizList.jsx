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
            <div>now loading..</div>
        );
    } else {
        return (
            <div>
                {quizzes.map(function (quiz) {
                    return <Quiz
                        key={quiz['id']}
                        id={quiz['id']}
                        author={quiz['user']['username']}
                        state="solved"
                        title={quiz['title']}
                        timestamp={formatTime(quiz['created_at'])}
                        star={quiz['gained_stars'].length}
                    />
                })}
            </div>
        );
    }
}

function Quiz({ id, author, state, title, timestamp, star }) {
    const current_url = location.href;
    const target_url = `${current_url}quiz/${id}`;
    return (
        <div className="pb-6 pt-3 px-8 mb-3 bg-slate-700 rounded-lg">
            <div class="mb-4">
                <div className="text-emerald-300 inline mr-2">
                    <CheckCircleIcon className="inline w-4 h-4 mr-1" />
                    {state}
                </div>
                <div className="inline">
                    <StarIcon className="inline w-4 h-4 mr-1" />
                    {star}
                </div>
            </div>
            <div className="text-sky-300 font-bold text-2xl mb-2">
                <a href={target_url} className="hover:text-sky-500">{title}</a>
            </div>
            <div className="text-right text-xs">
                <span className="text-slate-400 mr-2">{author}</span>
                <span className="">{timestamp}</span>
            </div>
        </div>
    );
}
const container = document.getElementById('root');
const root = ReactDOM.createRoot(container);
root.render(<App />);
