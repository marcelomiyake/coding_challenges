export function toRna(strand: string) {
  let rna = '';
  for (let nucleotide of strand) {
    rna = rna.concat(getRnaNucleotide(nucleotide));
  }
  return rna;
}

function getRnaNucleotide(nucleotide: string) {
  switch (nucleotide) {
    case 'G':
      return 'C';
    case 'C':
      return 'G';
    case 'T':
      return 'A';
    case 'A':
      return 'U';
    default:
      throw Error('Invalid input DNA.');
  }
}
