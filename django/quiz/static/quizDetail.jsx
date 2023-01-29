function QuizDetail({ id, title, content }) {
    return (
        <div className="py-6 px-8 mb-3 bg-slate-700 rounded-lg">
            <h2 className="text-2xl mb-4 font-bold text-sky-300">
                {title}
                <span className="ml-3 text-slate-400">#{ id }</span>
            </h2>
            <div className="[&>p]:mt-7 mb-16">{content}</div>
            <form action="" method="post">
                <div className="flex">
                    <button type="button" className="mx-4"></button>
                </div>
            </form>
        </div>
    );
}
