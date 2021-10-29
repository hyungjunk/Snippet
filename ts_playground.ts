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

 function hello(n: number) {
    console.log('outer is ', n)
    return (target:any, name:any, descriptor:any) => {
        console.log('original ', descriptor.value())
        descriptor.value = () => 1000
    }
}

class A {

    @hello(100)
    test() {
        return 55
    }
}

const a = new A();
const res = a.test();
console.log(res);

/**
 Defined type guard
*/

function isFish(pet: Fish | Bird): pet is Fish {
  return (pet as Fish).swim !== undefined;
}
