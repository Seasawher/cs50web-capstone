function QuizList() {
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
                <div>
                    {quizzes.map(function (quiz) {
                        return <Quiz
                            key={quiz['id']}
                            id={quiz['id']}
                            author={quiz['user']['username']}
                            state="attempted"
                            title={quiz['title']}
                            timestamp={formatTime(quiz['created_at'])}
                            star={quiz['gained_stars'].length}
                        />
                    })}
                </div>
            </div>
        );
    }
}

function State({ state }) {
    if (state == 'todo') {
        return (
            <div className="text-slate-400 inline mr-2">
                <span className="inline mr-1">-</span>
                {state}
            </div>
        );
    }
    if (state == 'attempted') {
        return (
            <div className="text-amber-300 inline mr-2">
                <ExclamationCircleIcon className="inline mr-1 w-4 h-4" />
                {state}
            </div>
        );
    }
    if (state == 'solved') {
        return (
            <div className="text-emerald-300 inline mr-2">
                <CheckCircleIcon className="inline w-4 h-4 mr-1" />
                {state}
            </div>
        );
    }
}

function Star({ star }) {
    const [starred, setStarred] = React.useState(false);

    function handleClick() {
        if (starred) {
            setStarred(false);
        } else {
            setStarred(true);
        }
    }

    if (! starred) {
        return (
            <button type="button" className="inline" onClick={handleClick}>
                <StarIcon className="inline w-4 h-4 mr-1" />
                {star}
            </button>
        );
    } else {
        return (
            <button type="button" className="inline text-amber-200" onClick={handleClick}>
                <SolidStarIcon className="inline w-4 h-4 mr-1" />
                {star+1}
            </button>
        );
    }
}

function Quiz({ id, author, state, title, timestamp, star }) {
    const current_url = location.href;
    const target_url = `${current_url}quiz/${id}`;

    return (
        <div className="pb-6 pt-3 px-8 mb-3 bg-slate-700 rounded-lg">
            <div className="mb-4">
                <State state={state} />
                <Star star={star}/>
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
