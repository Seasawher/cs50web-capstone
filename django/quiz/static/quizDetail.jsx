function QuizDetail({ id, title, content }) {
    return (
        <div className="py-6 px-8 mb-3 bg-slate-700 rounded-lg">
            <h2 className="text-2xl mb-4 font-bold text-sky-300">
                {title}
                <span className="ml-3 text-slate-400">#{id}</span>
            </h2>
            <div className="mb-4">
                <State state="todo" />
                <Star star="0" />
            </div>
            <div className="[&>p]:mt-7 mb-16">{content}</div>
            <form action="" method="post">
                <div className="flex">
                    <input className="focus:outline focus:outline-2 focus:outline-blue-500 focus:caret-blue-500
                        placeholder-gray-400 px-3 py-1 bg-gray-600 rounded-lg w-full"/>
                    <button type="button" className="mx-4">
                        <PaperAirplaneIcon className="inline w-7 h-7 hover:scale-110 hover:text-blue-200 text-blue-500" />
                    </button>
                </div>
            </form>
        </div>
    );
}
