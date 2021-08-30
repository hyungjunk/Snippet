/**
 * 제네릭을 활용한 자식 클래스 만들기
 * new ()
 */

export type Class<T> = new () => T;

interface Animal {
    // ...
}
class Dog implements Animal {
    // ...
}
function createAnimal<T extends Animal>(AnimalClass: new () => T): T {
    return new AnimalClass();
}
createAnimal(Dog); 


/**
 * 데코레이터
 */

