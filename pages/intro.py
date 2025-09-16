import streamlit as st

st.title("実験内容")

with st.container(border=True):
    st.header("実験説明")
    st.markdown(
        """
        本実験では、5〜10秒程度の発話音声のペアを聞いた後、質問にご回答いただきます。

        本実験は、2つのセクションがあります。

        セクション１では、音声ペアについて以下を評価していただきます。
        - **イントネーションの自然さ**：イントネーションはどちらの方が人の自然な発話のように聞こえるか？
        - **明瞭性**：発話内容はどちらの方が聞き取りやすいか？

        セクション２では、音声ペアについて以下を評価していただきます。
        - **声の類似度**：イントネーションや明瞭さは無視し、2つの発話の声はどのくらい類似しているか？
        
        各質問にはラジオボタン式の選択肢があります。もっとも当てはまるものを選択してください。

        セクション1では15ペア、セクション2では20ペアを評価していただきます。全部で35ペアになります。
        
        所要時間は20分程度です。

        音声は一度だけ繰り返して聞くことができます。(最大2回)

        画面が大きすぎる・小さすぎる場合は、ブラウザのズーム機能（Ctrl/CMD＋「+」「-」キー）で拡大・縮小してください。
        """
    )

    st.header("実験の例")
    st.markdown(
        """
        以下に、使用するインタフェースの例を示します。

        音声を流し、スピーカーやイヤホンの動作を確認してください。
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
            "**声の類似度**について、音声AとBの声は似ていると思いますか",
            options=[
                "とても似ていない",
                "似ていない",
                "どちらとも言えない",
                "似ている",
                "とても似ている",
            ],
            index=None,
        )

    st.warning(
        "回答の仕方が明らかに不誠実と判断される場合は、報酬をお支払いできないことがあります。"
    )

next_button = st.button(label="実験へ")
if next_button:
    st.switch_page("pages/exp.py")
