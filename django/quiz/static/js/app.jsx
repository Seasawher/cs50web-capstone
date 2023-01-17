function App() {
    return (
        <div className="py-6 px-8 mb-3 text-center">
            <table className="table-auto inline">
                <thead className="border-b-2 border-slate-500 text-slate-500">
                    <tr className="text-left">
                        <th className="px-5 pb-3">Status</th>
                        <th className="pr-5 pb-3">Title</th>
                        <th className="pr-5 pb-3">Stars</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td className="py-3"></td>
                        <td className="py-3">the summary of the quiz content</td>
                        <td className="py-3"></td>
                    </tr>
                </tbody>
            </table>
        </div>
    );
}

const container = document.getElementById('root');
const root = ReactDOM.createRoot(container);
root.render(<App />);
