import streamlit as st

st.title("実験内容")

with st.container(border=True):
    st.header("実験説明")
    st.markdown(
        """
        本実験では、5〜10秒程度の発話音声を2つ聞いた後、質問にご回答いただきます。

        本実験には、2つのセクションがあります。

        セクション１では、2つの音声を聞き、以下の2点について印象評価をしていただきます。
        - **イントネーションの自然さ**：どちらの方が人の自然な発話のように聞こえるか？
        - **明瞭性**：どちらの方が発話内容を聞き取りやすいか？

        セクション２では、2つの音声を聞き、以下の点について印象評価をしていただきます。
        - **声の類似度**：イントネーションや明瞭さは無視し、2つの発話の声はどのくらい類似しているか？（同一人物の声に聞こえるか？）
        
        各質問にはラジオボタン式の選択肢があります。もっとも当てはまるものを選択してください。

        セクション1では15セット、セクション2では20セット、合計35セットを評価していただきます。
        
        所要時間は20分程度です。

        音声は繰り返して聞くことができますが、3回までお願いします。

        画面が大きすぎる、または小さすぎる場合は、ブラウザのズーム機能（Ctrl/CMD＋「+」「-」キー）で調整が可能です。
        """
    )

    st.header("実験ページの例")
    st.markdown(
        """
        実験のページは以下のように表示されます。

        音声の再生ボタンを押して、スピーカーやイヤホンの動作を確認してください。
        """
    )

    with st.container(border=True):
        st.subheader("自然さ・明瞭性")
        st.text(f"音声を聞いて、質問にお答えください。")
        cols = st.columns(2, border=True)
        cols[0].text("音声A")
        cols[0].audio(
            "https://wu-cloud-bucket.s3.ap-northeast-3.amazonaws.com/20250912-el2nl-voice-conversion/el2nl/qvc_ft_10k/audio/jvs001/099.wav"
        )
        cols[1].text("音声B")
        cols[1].audio(
            "https://wu-cloud-bucket.s3.ap-northeast-3.amazonaws.com/20250912-el2nl-voice-conversion/el2nl/qvc_ft_pair_flat_10k/audio/jvs001/099.wav"
        )
        intonation_choice = st.radio(
            "Q1: **イントネーションの自然さ**について、どちらの方が自然に聞こえますか？",
            options=[
                "A",
                "ややA",
                "どちらとも言えない",
                "ややB",
                "B",
            ],
            index=None,
            horizontal=True,
        )
        intelligibility_choice = st.radio(
            "Q2: **明瞭性**について，どちらの方が聞き取りやすいと感じますか?",
            options=[
                "A",
                "ややA",
                "どちらとも言えない",
                "ややB",
                "B",
            ],
            index=None,
            horizontal=True,
        )

    with st.container(border=True):
        st.subheader("声の類似度（イントネーションや明瞭度は無視）")
        st.text(f"音声を聞いて、質問にお答えください。")
        cols = st.columns(2, border=True)
        cols[0].text("音声A")
        cols[0].audio(
            "https://wu-cloud-bucket.s3.ap-northeast-3.amazonaws.com/20250912-el2nl-voice-conversion/el2nl/qvc_ft_10k/audio/jvs001/099.wav"
        )
        cols[1].text("音声B")
        cols[1].audio(
            "https://wu-cloud-bucket.s3.ap-northeast-3.amazonaws.com/20250912-el2nl-voice-conversion/el2nl/gt/audio/jvs001/099.wav"
        )
        sim_choice = st.radio(
            "**声の類似度**について、音声AとBの声は似ていると思いますか？（同一人物の声に聞こえるか？）",
            options=[
                "とても似ている",
                "似ている",
                "どちらとも言えない",
                "似ていない",
                "まったく似ていない",
            ],
            index=None,
        )

    st.warning(
        "回答の仕方が明らかに不誠実と判断される場合は、報酬をお支払いできないことがあります。問題文をよく読み、ご理解いただいた上でご回答ください。"
    )

next_button = st.button(label="実験へ")
if next_button:
    st.switch_page("pages/exp.py")
