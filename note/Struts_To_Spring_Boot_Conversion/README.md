# Struts to Spring Boot Conversion

이번엔 이번 프로젝트에서의 주요 작업인 **Struts 프레임워크를 Spring Boot로 변환**하는 작업에 대해 작성해 보고자 한다.
Struts는 한때 Java 웹 애플리케이션 개발의 주요 프레임워크였지만, 더 현대적이고 유연한 Spring Boot로의 전환이 요구되고 있다.

---

## 1. 변환 작업의 필요성

Struts는 2000년대 초반에 많이 사용되었지만, 현재는 더 이상 적극적으로 사용되지 않는 프레임워크다.  
이번 프로젝트에서 Spring Boot로 변환을 고려하게 된 주요 이유는 다음과 같다:

- **유지보수성**: Struts 기반 애플리케이션은 기술 스택이 오래되어 유지보수가 어렵다. 반면 Spring Boot는 강력한 커뮤니티 지원과 최신 기술 트렌드 반영이 용이하다.
- **생산성**: Spring Boot는 프로젝트 초기 설정을 간소화하고, 내장 서버와 의존성 관리 등으로 개발 생산성을 높여준다.

---

## 2. 변환 과정에서의 주요 단계

Struts에서 Spring Boot로 전환하는 과정은 애플리케이션 전반의 구조를 새롭게 설계하는 작업이다.  

주요 단계로는
### 1) Struts Action 클래스를 Spring MVC 컨트롤러로 변환
- **Struts Action 클래스**는 기존의 요청 처리 로직을 포함하고 있다. 이를 **Spring MVC의 @Controller**와 **@RequestMapping**으로 변환해야 한다.
- URL 매핑 및 요청 처리는 `web.xml` 파일에서 Spring Boot의 `application.properties` 또는 `application.yml`로 옮겨간다.

### 2) JSP와 뷰 처리
- Struts 기반 JSP 뷰는 그대로 사용할 수 있지만, Spring Boot의 **Thymeleaf** 또는 **Mustache**와 같은 최신 템플릿 엔진으로 전환하는 것이 더 권장된다. (그러나 이번 프로젝트에선 JSP를 유지한다..)
- JSTL 태그 라이브러리는 Spring Boot에서도 사용할 수 있으므로, 기존 코드 재사용이 가능하다.

### 3) DAO 및 서비스 계층 재설계
- Struts 기반 DAO(Data Access Object) 계층은 보통 Hibernate와 함께 사용되지만, Spring Data JPA로 전환하면 더 효율적이다.
- JDBC 연결 코드는 **Spring의 JdbcTemplate**으로 대체하거나 JPA를 사용하여 더 간결하게 처리할 수 있다.

### 4) 설정 파일 전환
- Struts의 설정 파일(`struts-config.xml`)은 Spring Boot의 **Java Config** 또는 **application.yml**로 변환된다.
- 의존성 주입은 Spring의 **@Autowired**와 **@Configuration**으로 처리하며, XML 기반 설정을 최소화한다.

### 5) Interceptor 변환
- Struts의 Interceptor는 Spring의 **HandlerInterceptor** 또는 **AOP(Aspect-Oriented Programming)**를 활용하여 변환한다.
- 기존 로직을 최대한 재활용하면서 Spring의 표준 방식에 맞춰 리팩터링한다.

---

## 3. 변환 작업 중 겪은 어려움과 해결 방안

변환 작업은 단순히 코드를 옮기는 작업이 아니라, 기존 애플리케이션의 특성을 이해하고 새로운 환경에 맞게 재설계하는 과정이 포함된다.  
지금까지 진행하며 느낀 주요 어려움은 다음과 같다:

### 1) 기존 코드의 의존성
- **문제점**: Struts에서 Spring Boot로 전환하려면 기존 코드의 의존성을 정확히 파악해야 한다. 특히 Struts Action 클래스에 비즈니스 로직이 혼합된 경우, 이를 분리하는 데 시간이 걸린다.
- **해결 방안**: 기존 로직을 DAO, Service, Controller로 분리하며 계층별 역할을 명확히 했다.  

### 2) JSP와 템플릿 엔진의 차이
- **문제점**: 기존 JSP에서 사용하던 태그 라이브러리가 Spring Boot 템플릿 엔진과 호환되지 않는 경우가 있었다.
- **해결 방안**: JSP 뷰를 유지하면서 점진적으로 오류가 나는 부분을 개선해 나갔다.

### 3) 테스트와 검증
- **문제점**: 변환 후 기존 기능이 제대로 작동하는지 확인하기 위한 테스트 코드가 부족했다.
- **해결 방안**: JUnit과 Spring Test를 활용해 통합 테스트를 작성하고, 변환된 로직이 예상대로 작동하는지 검증했다.

---

## 4. 앞으로의 계획

앞으로 다음과 같은 목표를 가지고 작업을 이어나갈 예정이다:

1. **Spring Boot의 최신 기술 적용**: Spring Security, Spring Data JPA, 그리고 REST API 설계 등을 활용하여 애플리케이션을 현대화할 계획이다.
2. **테스트 코드 강화**: 변환된 코드의 안정성을 높이기 위해, 지속적으로 테스트 커버리지를 확장할 예정이다.
3. **성능 최적화**: Spring Boot로 전환하면서 발생할 수 있는 성능 이슈를 분석하고 최적화할 계획이다.

---

## 결론

Struts에서 Spring Boot로의 전환하는 과정에서 Spring Boot의 강점을 더 깊이 이해하고, 유지보수성과 확장성을 극대화할 수 있는 기반을 만들고자 한다.  
이 작업이 끝난 후에는, 기존의 레거시 애플리케이션이 어떻게 현대적인 아키텍처로 탈바꿈했는지 되돌아보며 큰 성취감을 느낄 수 있을 것이다.
