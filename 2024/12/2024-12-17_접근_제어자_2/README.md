# 접근 제어자 2

오늘은 이전에 작성했던 **접근 제어자**에 대해 예시를 포함하여 좀 더 명확하게 정리하려고 한다. 접근 제어자는 객체지향 프로그래밍에서 클래스, 메서드, 변수 등의 접근 범위를 제어하기 위해 사용된다. 특히 **캡슐화**를 실현하는 중요한 도구이며, 코드의 보안성과 유지보수성을 높이는 역할을 한다.

---

## 접근 제어자의 종류

Java를 기준으로 접근 제어자는 네 가지가 있다:

| 접근 제어자     | 같은 클래스 | 같은 패키지 | 자식 클래스 | 다른 패키지 |
|----------------|------------|------------|------------|------------|
| **private**   | O          | X          | X          | X          |
| **default**   | O          | O          | X          | X          |
| **protected** | O          | O          | O          | X          |
| **public**    | O          | O          | O          | O          |

---

### 1. **private**

- **범위**: 같은 클래스 내에서만 접근이 가능하다.  
- **특징**: 가장 제한적인 접근 제어자이며, 외부 클래스에서 변수나 메서드를 직접 사용할 수 없도록 한다.
- **용도**: 클래스 내부에서만 사용되어야 하는 데이터나 메서드를 숨기기 위해 사용된다.

**예시:**
```java
public class Example {
    private int value;

    private void displayValue() {
        System.out.println("Value: " + value);
    }

    public void setValue(int value) {
        this.value = value; // Setter를 통해 접근
    }
}
```
`value`와 `displayValue()`는 `private`이므로 클래스 내부에서만 접근할 수 있다. 외부 클래스는 `setValue()` 메서드를 통해 값을 설정해야 한다.

---

### 2. **default (package-private)**

- **범위**: 같은 패키지 내의 클래스에서 접근 가능하다. 접근 제어자를 명시하지 않으면 `default`가 적용된다.  
- **특징**: 패키지 단위로 접근을 허용하기 때문에 협업이 필요한 패키지 내부에서 자주 사용된다.

**예시:**
```java
class PackageExample {
    void displayMessage() {
        System.out.println("This is a default access method.");
    }
}
```
`PackageExample` 클래스와 `displayMessage()` 메서드는 같은 패키지 내에서만 접근이 가능하다.

---

### 3. **protected**

- **범위**: 같은 패키지 또는 자식 클래스에서 접근 가능하다.  
- **특징**: 상속을 활용할 때 유용하게 사용된다. 다른 패키지에 있는 클래스라도 상속 관계라면 접근이 가능하다.

**예시:**
```java
package parent;

public class Parent {
    protected String message = "Hello from Parent";
}

package child;

import parent.Parent;

public class Child extends Parent {
    public void displayMessage() {
        System.out.println(message); // Protected 변수 접근 가능
    }
}
```
- `message`는 `protected`이므로 상속받은 `Child` 클래스에서 접근할 수 있다.

---

### 4. **public**

- **범위**: 모든 클래스에서 접근 가능하다.  
- **특징**: 접근에 제한이 없기 때문에 어디서든 접근이 가능하다.
- **용도**: 클래스, 메서드, 변수 등이 외부에서 사용될 수 있도록 공개할 때 사용된다.

**예시:**
```java
public class PublicExample {
    public void greet() {
        System.out.println("Hello, World!");
    }
}
```
`PublicExample` 클래스와 `greet()` 메서드는 모든 클래스에서 접근이 가능하다.

---

## 접근 제어자 사용 시 주의사항

1. **캡슐화 원칙 준수**  
   - 멤버 변수는 `private`으로 선언하고, 외부에서 접근할 수 있도록 `getter`와 `setter`를 제공하는 것이 좋다.  
   - 이는 데이터의 무결성을 보호하고, 유연한 데이터 관리를 가능하게 한다.

2. **default의 명확한 사용**  
   - `default` 접근 제어자는 같은 패키지에서만 접근이 가능하기 때문에 패키지 단위로 묶여 있는 코드에만 사용해야 한다.

3. **protected의 남용 방지**  
   - 상속 관계에서만 유용하므로 불필요하게 사용하면 코드의 캡슐화를 해칠 수 있다.

4. **public의 신중한 사용**  
   - **공개된 API나 메서드**는 언제든 다른 코드에서 사용될 수 있으므로 변경 시 큰 영향을 미칠 수 있다. 꼭 필요한 경우에만 `public`으로 선언하자.

---

## 결론

접근 제어자는 코드의 **보안성**, **유지보수성**, **캡슐화**를 높이기 위해 사용된다. `private`과 `public`은 자주 사용되지만, `default`와 `protected`는 상황에 따라 신중하게 사용해야 한다.

개발자는 접근 제어자를 통해 **불필요한 노출을 방지**하고, 코드의 **안정성**을 확보할 수 있다. 특히 협업 프로젝트나 대규모 시스템에서는 접근 제어자를 명확하게 설정하여 코드의 품질을 높이는 것이 중요하다.
