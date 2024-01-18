import React from "react"
import { FaRegFileWord } from "react-icons/fa"

function Main() {
  return (
    <main className="main">
      <div className="main_input">
        <h1>Форматирование word документа под стандарт</h1>
        <h3>Загрузите word файл, который нужно отформатировать</h3>
        <div className="doc_input-output">
          <FaRegFileWord className="word-icon" />
          <input
            type="file"
            id="docpicker"
            accept=".doc,.docx,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document"
          />
          <button>Отформатировать</button>
        </div>
      </div>
      <div className="main_output">
        <h3>Отформатированный файл</h3>
        <a href="/src/img/microsoft-word.png" download="farmatted_document">
          Скачать файл
        </a>
      </div>
    </main>
  )
}

export default Main
