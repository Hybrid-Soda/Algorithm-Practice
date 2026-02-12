package practice_kit;

import java.util.*;

public class 베스트앨범_42579 {

    class Song {
        int index;
        int play;

        Song(int index, int play) {
            this.index = index;
            this.play = play;
        }
    }

    public int[] solution(String[] genres, int[] plays) {
        // 장르별 곡 리스트, 재생수
        HashMap<String, List<Song>> genreSong = new HashMap<>();
        HashMap<String, Integer> genrePlay = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            String genre = genres[i];
            int play = plays[i];

            genreSong.computeIfAbsent(genre, k -> new ArrayList<>()).add(new Song(i, play));
            genrePlay.put(genre, genrePlay.getOrDefault(genre, 0) + play);
        }

        // 1. 장르별 총 재생수 기준 정렬
        List<String> sortedPlay = new ArrayList<>(genrePlay.keySet());
        sortedPlay.sort((g1, g2) -> genrePlay.get(g2) - genrePlay.get(g1));

        // 2, 3. 순회 및 장르 내 정렬
        List<Integer> answer = new ArrayList<>();
        for (String genre : sortedPlay) {
            List<Song> songs = genreSong.get(genre);

            songs.sort((s1, s2) -> {
                if (s1.play != s2.play)
                    return s2.play - s1.play; // 재생 수 내림차순
                return s1.index - s2.index; // 인덱스 오름차순
            });

            for (int i = 0; i < Math.min(2, songs.size()); i++)
                answer.add(songs.get(i).index);
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }
}
