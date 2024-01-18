import { spawn } from "child_process"
import fs from "fs"

// PLAN
// 1. Взять файл на вход
// 2. Сериализовать в JSON/XML/whatever
// 3. Пройтись по каждому элементу
// 4. Воссоздать документ, с учётом того что придумали старые пердуны
// 5. Сохранить в файл

// console.log(originalDocx)

async function main() {
  // const newDoc = await patchDocument(originalDocx)

  // fs.writeFileSync("./test_doc/test_file_fixed.docx", newDoc)

  const child = spawn("python3", ["./transform.py"])
}

main()
