# Elasticsearch

오늘은 **Elasticsearch**에 대해 정리하고자 한다. Elasticsearch는 오픈소스 검색 및 분석 엔진으로, 방대한 양의 데이터를 빠르게 검색하고 분석할 수 있는 강력한 도구이다. 다양한 데이터 유형(문서, 메트릭, 로그 데이터 등)을 효율적으로 저장, 검색 및 분석할 수 있는 기능을 제공하며, 대규모 애플리케이션에서 자주 사용된다.

---

## 1. Elasticsearch란?

Elasticsearch는 Apache Lucene 기반으로 구축된 분산형 검색 엔진으로, JSON 형식의 데이터를 저장하고 강력한 검색 및 집계 기능을 제공한다. 일반적으로 **ELK 스택**(Elasticsearch, Logstash, Kibana)의 중심으로 사용되며, 실시간 로그 분석, 검색 기능 강화, 데이터 시각화 등에 활용된다.

---

## 2. 주요 개념

### **1) Index**
- **정의**: 데이터가 저장되는 기본 단위로, 데이터베이스의 테이블과 비슷한 개념이다.
- **특징**: 하나의 인덱스는 여러 샤드(shard)로 구성될 수 있으며, 데이터는 샤드 단위로 분산 저장된다.

### **2) Document**
- **정의**: Elasticsearch에 저장되는 데이터의 최소 단위로, JSON 형식으로 표현된다.
- **특징**: 하나의 문서는 특정 인덱스에 저장되며, 고유 식별자(ID)를 가진다.

### **3) Shard**
- **정의**: 인덱스를 분할하여 저장하는 단위로, 데이터를 여러 노드에 분산해 저장할 수 있도록 도와준다.
- **특징**: 샤드는 두 가지 유형으로 나뉜다.
  - **Primary Shard**: 원본 데이터를 저장.
  - **Replica Shard**: 백업 데이터를 저장.

### **4) Cluster**
- **정의**: 여러 노드의 집합으로, 데이터 분산과 고가용성을 제공한다.
- **특징**: 하나의 클러스터는 기본적으로 단일 이름으로 식별되며, 모든 노드가 동일한 클러스터 이름을 공유한다.

---

## 3. Elasticsearch의 주요 기능

### **1) 검색**
Elasticsearch는 빠른 검색 속도를 자랑하며, 텍스트 분석, 키워드 검색, 필터링 등 다양한 검색 옵션을 제공한다.

- **예제**: 특정 키워드 검색
  ```json
  GET /index_name/_search
  {
    "query": {
      "match": {
        "field_name": "search_keyword"
      }
    }
  }
  ```

### **2) 집계**
데이터 분석에 강력한 집계(Aggregation) 기능을 제공하며, 통계, 히스토그램, 평균 등 다양한 메트릭을 계산할 수 있다.

- **예제**: 필드 값의 평균 계산
  ```json
  GET /index_name/_search
  {
    "aggs": {
      "average_value": {
        "avg": {
          "field": "numeric_field"
        }
      }
    }
  }
  ```

### **3) 스케일링**
샤드와 노드를 통해 데이터가 자동으로 분산 저장되며, 새로운 노드를 추가하면 클러스터가 자동으로 리밸런싱하여 스케일링을 수행한다.

---

## 4. Elasticsearch의 장점

- **빠른 검색 성능**: 분산형 아키텍처와 인덱싱 기능을 통해 대용량 데이터도 빠르게 검색 가능.
- **실시간 데이터 처리**: 새로운 데이터가 들어오면 실시간으로 검색 가능.
- **확장성**: 클러스터에 새로운 노드를 추가하여 쉽게 확장 가능.
- **유연한 데이터 모델링**: JSON 문서 기반으로 다양한 데이터 구조를 저장하고 처리 가능.

---

## 5. Elasticsearch 사용 시 주의사항

- **데이터 구조 설계 중요**: 효율적인 검색을 위해 데이터 모델링을 신중히 설계해야 한다.
- **샤드 설정**: 샤드의 수와 크기를 적절히 설정하지 않으면 성능 저하 및 관리 부담이 발생할 수 있다.
- **리소스 사용량**: 메모리 및 디스크 사용량이 많아질 수 있으므로 클러스터 모니터링이 필수적이다.
- **백업**: 데이터를 주기적으로 스냅샷으로 백업하여 데이터 손실을 방지해야 한다.

---

## 결론

Elasticsearch는 대용량 데이터를 검색하고 분석하는 데 매우 효과적인 도구이다. 특히, 실시간 검색과 분석이 필요한 시스템에서 필수적으로 사용된다. 하지만 클러스터 구성, 샤드 설계, 리소스 사용량 관리 등의 세부적인 설정이 중요하므로, 이를 고려하여 최적화된 환경에서 사용해야 한다.