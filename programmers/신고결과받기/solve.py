def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_list = {id_: [] for id_ in id_list}

    for rp in report:
        a, b = rp.split(" ")
        report_list[b].append(a)

    for report_ in report_list.values():
        if len(set(report_)) >= k:
            for recived_mail in report_:
                answer[id_list.index(recived_mail)] += 1
    return answer


if __name__ == "__main__":
    """
    id_list = ["muzi", "frodo", "apeach", "neo"], 
    report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
    k = 2
    ######
    id_list = ["con", "ryan"],
    report = ["ryan con", "ryan con", "ryan con", "ryan con"], 
    k = 3
    """
    tc = [
        {
            "id_list": ["muzi", "frodo", "apeach", "neo"],
            "report":["muzi frodo", "apeach frodo",
                      "frodo neo", "muzi neo", "apeach muzi"],
            "k":2
        },
        {
            "id_list": ["con", "ryan"],
            "report":["ryan con", "ryan con", "ryan con", "ryan con"],
            "k":3
        }]
    for tc_ in tc:
        print(solution(tc_["id_list"], tc_["report"], tc_["k"]))
