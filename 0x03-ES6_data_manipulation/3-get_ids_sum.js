export default function getStudentIdsSum(students) {
  return students.reduce((sum, i) => sum + i.id, 0);
}
