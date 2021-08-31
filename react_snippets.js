/**
 * Component Composition.
 */
const TodoList = R.compose(Container, List, R.map(ListItem), items)