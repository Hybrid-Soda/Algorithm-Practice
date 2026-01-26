package practice_kit;

import java.util.HashSet;
import java.util.List;

public class 완주하지_못한_선수_42576 {

    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashSet<String> completionSet = new HashSet<>(List.of(completion));

        for (String person: participant) {
            if (completionSet.contains(person)) {
                completionSet.remove(person);
            } else {
                answer = person;
                break;
            }
        }

        return answer;
    }
}
