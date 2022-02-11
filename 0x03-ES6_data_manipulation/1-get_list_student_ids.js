export default function getListStudentIds(array) {
  if (!array.isArray(array)) return [];
  return array.map((i) => i.id);
}
