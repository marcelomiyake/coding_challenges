export function generateDocument(characters: string, document: string) {
  let charactersArray = characters.split('');
  let documentArray = document.split('');
  for (let c of documentArray) {
    let existChar = false;
    for (let i = 0; i < charactersArray.length; i++) {
      if (charactersArray[i] === c) {
        charactersArray.splice(i, 1);
        existChar = true;
        break;
      }
    }
    if (!existChar) {
      return false;
    }
  }
  return true;
}
