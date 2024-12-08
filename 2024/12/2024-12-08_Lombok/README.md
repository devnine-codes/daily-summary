# Lombok: Java 개발자의 필수 도구

오늘은 **Lombok**에 대해 작성하려 한다.  
Lombok은 Java 개발에서 보일러플레이트 코드(반복적인 코드)를 줄여주는 강력한 라이브러리다.  
@Getter, @Setter, @Builder 같은 어노테이션을 활용하면 코드 가독성과 생산성을 동시에 높일 수 있다.  
많은 Java 프로젝트에서 Lombok은 필수적인 도구로 자리 잡고 있다.

---

## 1. Lombok이란?

Lombok은 Java 클래스에서 **반복적인 코드**를 자동으로 생성해주는 라이브러리다.  
예를 들어, getter/setter 메서드, toString(), equals(), hashCode() 등의 메서드는 Java 개발에서 필수적이지만 반복적으로 작성해야 하는 번거로움이 있다.  
Lombok은 이러한 코드를 어노테이션 한 줄로 대체해준다.

---

## 2. Lombok의 주요 어노테이션

### **1) @Getter와 @Setter**
- **@Getter:** 필드의 getter 메서드를 자동으로 생성.
- **@Setter:** 필드의 setter 메서드를 자동으로 생성.  
  그러나 **setter 사용은 주의가 필요**하다. (아래 참고)

```java
@Getter
@Setter
public class User {
    private String name;
    private int age;
}
```

### **2) @ToString**
- toString() 메서드를 자동 생성.
- 특정 필드를 제외하거나, 순서를 변경할 수도 있다.

```java
@ToString
public class User {
    private String name;
    private int age;
}
```

### **3) @EqualsAndHashCode**
- equals()와 hashCode() 메서드를 자동 생성.
- 객체 비교와 해싱 작업에 유용.

```java
@EqualsAndHashCode
public class User {
    private String name;
    private int age;
}
```

### **4) @NoArgsConstructor, @AllArgsConstructor, @RequiredArgsConstructor**
- **@NoArgsConstructor:** 기본 생성자를 자동 생성.
- **@AllArgsConstructor:** 모든 필드를 포함하는 생성자를 자동 생성.
- **@RequiredArgsConstructor:** `final`이나 `@NonNull` 필드만 포함하는 생성자를 생성.

### **5) @Builder**
- 빌더 패턴을 자동으로 구현.
- 객체 생성 시 가독성을 높이고, 유연하게 필드를 설정할 수 있다.

```java
@Builder
public class User {
    private String name;
    private int age;
}
User user = User.builder()
                .name("John")
                .age(30)
                .build();
```

---

## 3. Lombok 사용 시 주의사항

### **1) @Setter 사용 주의**
`@Setter`는 모든 필드에 setter 메서드를 생성하지만, 객체의 **캡슐화 원칙**을 해칠 수 있으므로 주의가 필요하다.

#### 문제점:
- **불필요한 값 변경 허용:** 외부에서 필드 값을 마음대로 수정할 수 있다.
- **객체 불변성 손상:** mutable(변경 가능) 상태가 되어 동시성 문제를 유발할 수 있다.

#### 대안:
- 필요한 경우에만 개별 필드에 `@Setter`를 추가하거나, 명시적인 메서드로 값 변경을 제한하라.

```java
public class User {
    private final String name;
    private int age;

    // 필요한 경우에만 setter
    @Setter
    private String email;

    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void incrementAge() {
        this.age++;
    }
}
```

---

### **2) 의존성 추가**
Lombok을 사용하려면 프로젝트에 의존성을 추가해야 한다.

**Maven:**
```xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.36</version>
    <scope>provided</scope>
</dependency>
```

**Gradle:**
```groovy
implementation 'org.projectlombok:lombok:1.18.36'
annotationProcessor 'org.projectlombok:lombok:1.18.36'
```

---

### **3) IDE 설정**
IntelliJ IDEA나 Eclipse와 같은 IDE에서 Lombok 플러그인을 설치하고 설정해야 한다.

---

### **4) 디버깅**
Lombok이 생성한 코드는 소스에서 보이지 않기 때문에 디버깅 시 혼란을 줄 수 있다.  
이를 보완하기 위해 IDE 설정에서 **컴파일된 클래스의 메서드**를 확인하는 것이 좋다.

---

## 4. Lombok의 장점

- **코드 간소화:** 반복적인 코드를 줄여 가독성과 생산성을 향상.
- **유지보수 용이:** 코드를 일일이 수정하지 않아도, 어노테이션으로 관리 가능.
- **가독성 향상:** 핵심 로직에 집중할 수 있다.

---

## 5. Lombok 활용하며 느낀 점

Lombok은 처음에는 자동 생성된 메서드가 보이지 않아 혼란스러웠지만, 익숙해지면 생산성을 크게 향상시키는 도구다.  
특히 `@Builder`와 `@Data`는 자주 사용하며, 반복적인 코드를 없애주는 데 매우 유용했다.  
다만, 지나치게 의존하지 않고 필요한 경우에만 사용하는 것이 Lombok의 효과를 극대화하는 방법이라고 느꼈다.

---

## 결론

Lombok은 Java 개발자에게 반복적인 작업을 줄여주는 강력한 도구다.  
하지만 모든 프로젝트에 무조건 도입하기보다는 팀원과의 협의 및 코드 스타일에 맞춰 적절히 사용하는 것이 중요하다.  
캡슐화 원칙을 지키며 `@Setter`와 같은 어노테이션의 사용을 신중히 고민해야 한다.